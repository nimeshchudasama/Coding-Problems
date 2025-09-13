import NavBar from './components/NavBar'
import MenuCard from './components/MenuCard'
import './App.css'

function App() {
  return (
    <>
      <NavBar />
      <main className="content">
        <h1>Welcome to Our Restaurant</h1>
        <MenuCard />
      </main>
    </>
  )
}

export default App
