import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

function App() {

  return (
    <div className="w-full h-screen flex">
        <main className="w-full h-fit m-10 rounded-md border-1">
            <Navbar />
            <Hero />
        </main>
    </div>
  )
}

export default App
