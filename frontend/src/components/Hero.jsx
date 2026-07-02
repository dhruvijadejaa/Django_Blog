import axios from "axios";
import React, { useState, useEffect } from "react";

const Hero = () => {
  const [featured, setFeatured] = useState([]);

  useEffect(() => {
    const isFeatured = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/featured/");
        setFeatured(response.data);
        console.log(response.data);
      } catch (error) {
        console.log("wrong with featured");
      }
    };
    isFeatured();
  }, []);
  return (
  <section className="w-full">

    {featured && (
      <div className="relative w-full h-[400px] overflow-hidden p-4">

        {/* Image */}
        <img
          src={featured.featured_image}
          className="w-full h-full object-cover"
        />

        {/* Overlay */}
        <div className="absolute inset-0 bg-black/40 flex flex-col justify-center p-6">

          <h1 className="text-white text-3xl font-bold">
            {featured.title}
          </h1>

          <p className="text-white mt-2">
            {featured.short_description}
          </p>

        </div>

      </div>
    )}

  </section>
)
};

export default Hero;
