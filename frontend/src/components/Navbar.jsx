import React, { useState, useEffect } from "react";
import axios from "axios";

const Navbar = () => {
  const [categories, setcategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/api/categories/",
        );
        setcategories(response.data);
      } catch (error) {
        console.log("something went wrong");
      }
    };
    fetchCategories();
  }, []);
  return (
    <div>
      <div className="title-bar h-9 w-full items-center flex justify-between items-center">
        <h1 className="title-bar-text">Django Blog </h1>
        <div className="flex  gap-6 items-center">
          <button className="mt-0.5 p-1 rounded-md cursor-pointer">
            Log in
          </button>
          <button className=" mt-0.5 p-1 rounded-md cursor-pointer">
            Sign up
          </button>
        </div>
      </div>

      <nav className="w-full flex  cursor-pointer">
        <ul role="menubar" className="flex w-full justify-around gap-5">
          {categories.map((category) => (
            <li key={category.id} role="menuitem">
              <a href="#" className="text-black hover:text-black">{category.category_name}</a>
            </li>
          ))}
        </ul>
      </nav>

      <div className="relative w-full h-[200px] overflow-hidden">
        <video
          autoPlay
          loop
          muted
          playsInline
          src="./media/videos/newyork.mp4"
          className="absolute inset-0 w-full h-[200px] object-cover blur-xs  "
        >
          This is video
        </video>

        <div className="absolute inset-0 bg-black/40"></div>

        <div className="relative z-10 h-full flex justify-center items-center">
          <h1 className="font-bold text-white text-6xl">WELCOME TO THE BLOG</h1>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
