import './NavBar.css'

const NavBar = () => (
  <nav className="navbar">
    <ul>
      <li><a href="#events">Events</a></li>
      <li><a href="#catering">Catering</a></li>
      <li><a href="#about">About Us</a></li>
      <li><a href="#menu">Menu</a></li>
      <li><a href="#location">Location</a></li>
      <li className="dropdown">
        <span>Delivery</span>
        <ul className="dropdown-content">
          <li><a href="https://www.doordash.com" target="_blank" rel="noopener noreferrer">DoorDash</a></li>
          <li><a href="https://www.ubereats.com" target="_blank" rel="noopener noreferrer">Uber Eats</a></li>
        </ul>
      </li>
      <li><a className="order-button" href="https://www.toasttab.com" target="_blank" rel="noopener noreferrer">Order Online</a></li>
    </ul>
  </nav>
)

export default NavBar

