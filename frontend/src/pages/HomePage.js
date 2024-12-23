import React, { useEffect, useState } from 'react';
import axios from 'axios';

function HomePage() {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/store/api/categories/');
        setCategories(response.data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchCategories();
  }, []);

  if (loading) return <p className="loading">Загрузка...</p>;
  if (error) return <p className="error">Ошибка: {error}</p>;

  return (
    <div className="container">
      <h1>Добро пожаловать в СТИМАП!</h1>
      <p>Здесь вы найдете ключи для любимых игр по лучшим ценам.</p>
      <h2>Категории:</h2>
      <ul>
        {categories.map((category) => (
          <li key={category.id}>{category.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
