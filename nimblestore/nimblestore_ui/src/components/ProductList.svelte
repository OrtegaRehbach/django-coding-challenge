<script>
    import { onMount } from 'svelte';
    let products = [];
    const apiURL = 'http://127.0.0.1:8000/api';

    async function fetchProducts() {
        try {
            const response = await fetch(`${apiURL}/products/`);
            products = await response.json();
        } catch (error) {
            console.error('Error fetching products:', error);
        }
    }

    onMount(fetchProducts);
</script>

<button on:click={fetchProducts}>Refresh Products</button>
<div class="product-container">
    {#each products as product}
        <div class="product">
            Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}
        </div>
    {/each}
</div>

<style>
    .product-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .product {
        border: 1px solid #000;
        margin: 10px;
        padding: 10px;
    }
</style>