import { Inter } from "next/font/google";
import "./globals.css";
import Logo from "./Images/Logo.jpg";
import profileIcon from "./Images/profileIcon.png"

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Home | Mod Auto Gallery",
  description: "This is the home page for Mod Auto Gallery, a website that you can post your personal automotive builds including photos, videos, and mod list/description! Join up and start those uploads!",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div>
          <nav className="bg-[#202124] text-white grid grid-flow-row grid-cols-2">
            <div>
              <img className="w-14 rounded-full m-3" src={Logo.src} alt="Murdered out GT-R" />
            </div>
            <div className="flex items-center justify-end">
              <ul className="flex mr-10 font-bold text-2xl gap-10">
                <li className="transition-colors duration-300 hover:text-[#FF5C00]"><a href="#">Home</a></li>
                <li className="transition-colors duration-300 hover:text-[#FF5C00]"><a href="#">Gallery</a></li>
                <li className="transition-colors duration-300 hover:text-[#FF5C00]"><a href="#">Upload</a></li>
                <li className="w-10"><a href="#"><img className="rounded-full" src={profileIcon.src} alt="Profile Icon"></img></a></li>
              </ul>
            </div>
          </nav>
        </div>
        {children}
        <div>
          <footer className="bg-[#202124] text-white">
            <p>This will be the footer</p>
          </footer>
        </div>
      </body>
    </html>
  );
}
