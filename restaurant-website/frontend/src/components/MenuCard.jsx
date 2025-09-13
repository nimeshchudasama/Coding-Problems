import './MenuCard.css'

function MenuCard() {
  return (
    <section className="menu-card">
      <h2>Indian Favorites</h2>
      <ul>
        <li>
          <span className="item">Butter Chicken</span>
          <span className="price">$12.99</span>
        </li>
        <li>
          <span className="item">Palak Paneer</span>
          <span className="price">$10.99</span>
        </li>
        <li>
          <span className="item">Vegetable Biryani</span>
          <span className="price">$11.99</span>
        </li>
        <li>
          <span className="item">Garlic Naan</span>
          <span className="price">$3.99</span>
        </li>
      </ul>
    </section>
  )
}

export default MenuCard
