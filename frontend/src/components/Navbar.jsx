import "./Navbar.css";
import { Link } from "react-router-dom";
function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Image Analyzer</div>
      <div className="navbar-menu">
        <a href="/">Home</a>
        <Link to="/checktype">File format</Link>
        <Link to="/checkdetail">Metadata</Link>
        <Link to="/checkreliability">Analysis</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
}

export default Navbar;
