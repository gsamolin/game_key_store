import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { CartContext } from '../contexts/CartContext';

function CatalogPage() {
  const { addToCart, cart } = useContext(CartContext);
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log('Корзина обновлена (CatalogPage):', cart);
  }, [cart]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/store/api/products/');
        setProducts(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchProducts();
  }, []);
  
  if (loading) return <p>Загрузка...</p>;
  if (error) return <p>Ошибка: {error}</p>;

  return (
    <div className="container">
      <h1>Каталог</h1>
      <ul className="catalog-list">
        {products.map((product) => (
          <li key={product.id} className="catalog-item">
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>Цена: {product.price} руб.</p>
            <button onClick={() => addToCart(product)}>Добавить в корзину</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CatalogPage;
