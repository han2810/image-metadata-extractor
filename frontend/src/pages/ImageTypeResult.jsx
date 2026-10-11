import "./ImageTypeResult.css";
import Navbar from "../components/Navbar.jsx";
import { useLocation } from "react-router-dom";
function ResultBox() {
  const location = useLocation();
  const data = location.state;
  return (
    <>
      <Navbar />
      <div className="result-box">
        <h2>Inspection result:</h2>
        <p className="content">
          <strong className="title">File name: </strong>
          {data.name}
        </p>
        <p className="content">
          <strong className="title">File type: </strong>
          {data.type}
        </p>
      </div>
    </>
  );
}
export default ResultBox;
