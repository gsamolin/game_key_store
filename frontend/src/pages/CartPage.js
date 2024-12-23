import React, { useContext } from 'react';
import { CartContext } from '../contexts/CartContext';

function CartPage() {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);


  if (cart.length === 0) {
    return (
      <div>
        <h1>Корзина</h1>
        <p>Ваша корзина пуста.</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Корзина</h1>
      <ul>
        {cart.map((item) => (
          <li key={item.id}>
            <h3>{item.name}</h3>
            <p>Количество: {item.quantity}</p>
            <p>Цена за единицу: {item.price} руб.</p>
            <p>Общая цена: {item.quantity * item.price} руб.</p>
            <button onClick={() => removeFromCart(item.id)}>Удалить</button>
          </li>
        ))}
      </ul>
      <button onClick={clearCart}>Очистить корзину</button>
    </div>
  );
}

export default CartPage;
