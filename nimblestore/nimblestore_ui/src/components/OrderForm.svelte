<script>
    import { onMount } from 'svelte';
    let products = [{ name: '', quantity: 1 }];
    const apiURL = 'http://127.0.0.1:8000/api';

    function addProduct() {
        products = [...products, { name: '', quantity: 1 }];
    }

    async function submitOrder(event) {
        event.preventDefault();
        try {
            const response = await fetch(`${apiURL}/order/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(products),
            });
            const data = await response.json();
            alert(`Total cost of order: ${data.total}`);
        } catch (error) {
            console.error('Error submitting order:', error);
        }
    }
</script>

<form on:submit={submitOrder}>
    {#each products as product, index}
        <div>
            <label for="product-name-{index}">Product Name:</label><br>
            <input
                type="text"
                id="product-name-{index}"
                bind:value={product.name}
                required
            /><br>
            <label for="quantity-{index}">Quantity:</label><br>
            <input
                type="number"
                id="quantity-{index}"
                bind:value={product.quantity}
                min="1"
                required
            /><br>
        </div>
    {/each}
    <button type="button" on:click={addProduct}>Add Another Product</button><br>
    <input type="submit" value="Submit Order" />
</form>