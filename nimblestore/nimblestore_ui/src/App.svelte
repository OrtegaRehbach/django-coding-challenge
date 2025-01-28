<script>
    import ProductList from './components/ProductList.svelte';
    import OrderForm from './components/OrderForm.svelte';
</script>

<main>
    <h1>Product List</h1>
    <ProductList />

    <h2>Place an Order</h2>
    <OrderForm />
</main>

<style>
    main {
        font-family: Arial, sans-serif;
        padding: 20px;
    }
</style>