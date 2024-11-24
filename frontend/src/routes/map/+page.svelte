<script>
    import { onMount } from 'svelte';
    import { Button, Spinner } from 'flowbite-svelte';

    let map;
    let markers = [];
    let mapCenter = { lat: 43.4643, lng: -80.5204 }; // Default to Waterloo, Canada in case geolocation fails
    let loading = true; // Set loading to true initially
    let selectedStyle = "silver"; // Default to silver styling

    const styles = {
        silver: [
            {
                elementType: "geometry",
                stylers: [{ color: "#f5f5f5" }],
            },
            {
                elementType: "labels.icon",
                stylers: [{ visibility: "off" }],
            },
            {
                elementType: "labels.text.fill",
                stylers: [{ color: "#616161" }],
            },
            {
                elementType: "labels.text.stroke",
                stylers: [{ color: "#f5f5f5" }],
            },
            {
                featureType: "administrative.land_parcel",
                elementType: "labels.text.fill",
                stylers: [{ color: "#bdbdbd" }],
            },
            {
                featureType: "poi",
                stylers: [{ visibility: "off" }],
            },
            {
                featureType: "poi",
                elementType: "geometry",
                stylers: [{ color: "#eeeeee" }],
            },
            {
                featureType: "poi.park",
                elementType: "geometry",
                stylers: [{ color: "#e5e5e5" }],
            },
            {
                featureType: "transit",
                stylers: [{ visibility: "off" }],
            },
            {
                featureType: "road",
                elementType: "geometry",
                stylers: [{ color: "#ffffff" }],
            },
            {
            featureType: "road.arterial",
            elementType: "labels.text.fill",
            stylers: [{ color: "#757575" }],
            },
            {
            featureType: "road.highway",
            elementType: "geometry",
            stylers: [{ color: "#dadada" }],
            },
            {
                featureType: "water",
                elementType: "geometry",
                stylers: [{ color: "#c9c9c9" }],
            },
        ],
        dark: [
            {
                elementType: "geometry",
                stylers: [{ color: "#212121" }],
            },
            {
                elementType: "labels.icon",
                stylers: [{ visibility: "off" }],
            },
            {
                elementType: "labels.text.fill",
                stylers: [{ color: "#757575" }],
            },
            {
                elementType: "labels.text.stroke",
                stylers: [{ color: "#212121" }],
            },
            {
                featureType: "poi",
                stylers: [{ visibility: "off" }],
            },
            {
                featureType: "road",
                elementType: "geometry",
                stylers: [{ color: "#373737" }],
            },
            {
                featureType: "water",
                elementType: "geometry",
                stylers: [{ color: "#000000" }],
            },
        ],
    };

    async function getUserLocation() {
        return new Promise((resolve, reject) => {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    (position) => {
                        resolve({
                            lat: position.coords.latitude,
                            lng: position.coords.longitude,
                        });
                    },
                    (error) => {
                        console.error("Error getting location:", error);
                        reject(error);
                    }
                );
            } else {
                reject(new Error("Geolocation is not supported by this browser."));
            }
        });
    }

    async function initializeMap() {
        const { Map } = await google.maps.importLibrary("maps");

        map = new Map(document.getElementById("map"), {
            center: mapCenter,
            zoom: 15,
            styles: styles[selectedStyle], // Apply the selected style
        });

        loading = false; // Set loading to false after the map is initialized
    }

    function updateMapStyle(style) {
        selectedStyle = style;
        if (map) {
            map.setOptions({ styles: styles[style] });
        }
    }

    async function createMarker(place) {
    const { InfoWindow } = await google.maps.importLibrary("maps");

    const marker = new google.maps.Marker({
        map,
        position: place.geometry.location,
        title: place.name,
    });

    const infoWindow = new InfoWindow({
        content: `
            <div>
                <h3>${place.name}</h3>
                <p>${place.vicinity}</p>
            </div>
        `,
    });

    // Add a click listener to open the InfoWindow when the marker is clicked
    marker.addListener("click", () => {
        infoWindow.open(map, marker);
    });

    markers.push(marker);
}   

async function fetchNearbyPlaces(type) {
    markers.forEach((marker) => marker.setMap(null)); // Clear existing markers
    markers = [];

    // Get the current center of the map dynamically
    const currentCenter = map.getCenter();
    const location = {
        lat: currentCenter.lat(),
        lng: currentCenter.lng(),
    };

    const { PlacesService, PlacesServiceStatus } = await google.maps.importLibrary("places");
    const service = new PlacesService(map);

    const request = {
        location, // Use the updated location
        radius: 1000, // Search within 1km
        type,
    };

    service.nearbySearch(request, (results, status) => {
        if (status === PlacesServiceStatus.OK) {
            results.forEach(createMarker);
        }
    });
}

    onMount(async () => {
        try {
            // Request user's location
            mapCenter = await getUserLocation();
        } catch (error) {
            console.warn("Using default location:", mapCenter);
        }

        if (!window.google) {
            const script = document.createElement("script");
            script.src = `https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY`;
            script.async = true;
            script.defer = true;
            script.onload = initializeMap;
            document.body.appendChild(script);
        } else {
            await initializeMap();
        }
    });
</script>

<style>
    #map {
        width: 100%;
        height: 500px;
        border-radius: 0.5rem;
    }

    .button-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1rem;
    }

    .spinner-overlay {
        position: fixed;
        inset: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 50;
    }

    .style-selector {
        margin: 1rem auto;
        text-align: center;
    }
</style>

<div>
    <!-- Spinner -->
    {#if loading}
        <div class="spinner-overlay">
            <Spinner color="purple" size={10} />
        </div>
    {/if}

    <!-- Style Selector -->
    <div class="style-selector">
        <label for="style" class="p-4 text-gray-900 dark:text-gray-100">Select Map Style:</label>
        <select id="style" on:change={(e) => updateMapStyle(e.target.value)}>
            <option value="silver">Silver</option>
            <option value="dark">Dark</option>
        </select>
    </div>

    <!-- Map Container -->
    <div id="map"></div>

    <!-- Buttons -->
    <div class="button-container">
        <Button class="p-4 text-gray-900 dark:text-gray-100" color="info" style="margin-bottom: 1%" on:click={() => fetchNearbyPlaces("restaurant")}>Find Restaurants</Button>
        <Button class="p-4 text-gray-900 dark:text-gray-100" color="info" style="margin-bottom: 1%" on:click={() => fetchNearbyPlaces("lodging")}>Find Hotels</Button>
        <Button class="p-4 text-gray-900 dark:text-gray-100" color="info" style="margin-bottom: 1%" on:click={() => fetchNearbyPlaces("toilet")}>Find Toilets</Button>
    </div>
</div>
