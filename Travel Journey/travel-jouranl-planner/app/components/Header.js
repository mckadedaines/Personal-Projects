"use client";
import React, { useState } from "react";

function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  function toggleMenu() {
    setIsMenuOpen(!isMenuOpen);
  }

  return (
    <div>
      <header className="bg-blue-400 pt-5 pb-5 flex items-center justify-between m-5 rounded-xl">
        <img
          className="w-16 h-16 md:w-20 md:h-20 ml-4 md:ml-8 rounded-full"
          src="/images/logo.png"
          alt="logo"
        />
        <button
          className="md:hidden p-2 z-50"
          onClick={toggleMenu}
          aria-label="Toggle menu"
        >
          <span className="text-2xl">{isMenuOpen ? '✕' : '☰'}</span>
        </button>
        <nav
          className={`fixed inset-0 bg-blue-400 transform ${
            isMenuOpen ? "translate-x-0" : "translate-x-full"
          } transition-transform duration-300 ease-in-out z-40 md:flex md:items-center md:justify-end md:static md:translate-x-0`}
        >
          <ul className="list-none flex flex-col md:flex-row items-center gap-8 text-2xl text-white p-4 mr-3 md:p-0">
            <li>
              <a
                className="transition duration-300 font-bold hover:text-yellow-400 hover:bg-white hover:bg-opacity-20 p-3 rounded-md"
                href="#"
                onClick={toggleMenu}
              >
                Home
              </a>
            </li>
            <li>
              <a
                className="transition duration-300 font-bold hover:text-yellow-400 hover:bg-white hover:bg-opacity-20 p-3 rounded-md"
                href="#"
                onClick={toggleMenu}
              >
                Planner
              </a>
            </li>
            <li>
              <a
                className="transition duration-300 font-bold hover:text-yellow-400 hover:bg-white hover:bg-opacity-20 p-3 rounded-md"
                href="#"
                onClick={toggleMenu}
              >
                Journal
              </a>
            </li>
            <li>
              <a
                className="transition duration-300 font-bold hover:text-yellow-400 hover:bg-white hover:bg-opacity-20 p-3 rounded-md"
                href="#"
                onClick={toggleMenu}
              >
                Profile
              </a>
            </li>
          </ul>
        </nav>
      </header>
    </div>
  );
}

export default Header;
