import React, { useContext } from 'react';
import { CartContext } from '../contexts/CartContext';

function CartPage() {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);

  console.log('Текущая корзина (CartPage):', cart);

  if (cart.length === 0) {
    return (
      <div>
        <h1>Корзина</h1>
        <p>Ваша корзина пуста.</p>
      </div>
    );
  }

  return (
    <div className="container">
      <h1>Корзина</h1>
      {cart.length === 0 ? (
        <p>Ваша корзина пуста.</p>
      ) : (
        <>
          <ul className="cart-list">
            {cart.map((item) => (
              <li key={item.id} className="cart-item">
                <div>
                  <h3>{item.name}</h3>
                  <p>Количество: {item.quantity}</p>
                  <p>Цена за единицу: {item.price} руб.</p>
                  <p>Общая цена: {item.quantity * item.price} руб.</p>
                </div>
                <button onClick={() => removeFromCart(item.id)}>Удалить</button>
              </li>
            ))}
          </ul>
          <button className="clear-cart" onClick={clearCart}>
            Очистить корзину
          </button>
        </>
      )}
    </div>
  );
}

export default CartPage;
