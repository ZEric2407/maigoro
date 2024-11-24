<script>
    import { onMount } from 'svelte';
    import { Gallery } from 'flowbite-svelte';
    const images = [];

    const getTransactions = async () => {
        try {
        const response = await fetch('http://localhost:5000/api/gallery', {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            },
        });
    
        if (response.ok) {
            const data = await response.json();
            console.log('Backend response:', data);
            for (let i = 0; i< data.transactions.length; i++) {
                images.push({
                    alt: i,
                    src: "/../backend/" + data.transactions[i].image_url.replace("\\", "/")
                })
                alert(images[i].src)
            }
            return data;
        } else {
            console.error('Error sending image to backend:', response.statusText);
        }
        } catch (error) {
        console.error('Error during backend call:', error);
        }
    };

    onMount(async () => {
        await getTransactions();
    });
</script>
  
<Gallery items={images} class="gap-4 grid-cols-2 md:grid-cols-3"/>