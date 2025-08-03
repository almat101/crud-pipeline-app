import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductPage = () => {
    const [products, setProducts] = useState([]); // List of all products
    const [product] = useState(null); // Single product by ID
    const [addFormData, setAddFormData] = useState({ name: '', price: '', category: '', user_id: '' }); // For POST
    const [delProductId, setDeleteProductId] = useState(''); // ID for DELETE
    const [message, setMessage] = useState(''); // Success/Error messages

    // Fetch all products
    const fetchProducts = async () => {
        try {
            const response = await axios.get('/api/products');
            setProducts(response.data);
        } catch (error) {
            setMessage('Failed to fetch products');
        }
    };


    // Add a new product
    const addProduct = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/products', addFormData);
            setMessage('Product added successfully!');
            console.log(response)
            fetchProducts(); // Refresh the product list
        } catch (error) {
            setMessage('Failed to add product');
        }
    };

  

    // Delete a product
    const deleteProduct = async () => {
        try {
            await axios.delete(`/api/products/${delProductId}`);
            setMessage('Product deleted successfully!');
            fetchProducts(); // Refresh the product list
        } catch (error) {
            setMessage('Failed to delete product');
        }
    };

    // Fetch all products on component mount
    useEffect(() => {
        fetchProducts();
    }, []);

    return (
        <div>
            <h1>Product Management</h1>
            {message && <p>{message}</p>}
            {/* List all products */}
            <h2>All Products</h2>
            <ul style={{ listStyleType: 'none' }}>
             <li>
                <strong>ID</strong> - <strong>Name</strong> - <strong>Price</strong> - <strong>Category</strong> - <strong>User ID</strong>
            </li>
                {products.map((prod) => (
                    <li key={prod.id}>
                    {prod.id} - {prod.name} - ${prod.price} - {prod.category} - {prod.user_id}
                    </li>
                ))}
            </ul>



            {/* Add a new product */}
            <h2>Add Product</h2>
            <form onSubmit={addProduct}>
                <input
                    type="text"
                    placeholder="Name"
                    value={addFormData.name}
                    onChange={(e) => setAddFormData({ ...addFormData, name: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="Price"
                    value={addFormData.price}
                    onChange={(e) => setAddFormData({ ...addFormData, price: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Category"
                    value={addFormData.category}
                    onChange={(e) => setAddFormData({ ...addFormData, category: e.target.value })}
                />
                <input
                    type="number"
                    placeholder="User_id"
                    value={addFormData.user_id}
                    onChange={(e) => setAddFormData({ ...addFormData, user_id: e.target.value })}
                />
                <button type="submit">Add Product</button>
            </form>

           
            {/* Delete a product */}
            <h2>Delete Product</h2>
            <input
                type="number"
                placeholder="Delete Product ID"
                value={delProductId}
                onChange={(e) => setDeleteProductId(e.target.value)}
            />
            <button onClick={deleteProduct}>Delete Product</button>
             {product && (
                <div>
                    <h3>Product Details</h3>
                    <p>Name: {product.name}</p>
                    <p>Price: {product.price}</p>
                    <p>Category: {product.category}</p>
                    <p>User id: {product.user_id}</p>
                </div>
            )}
        </div>
    );
};

export default ProductPage;