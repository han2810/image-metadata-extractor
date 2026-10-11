import "./ResultBox.css";
import "./Navbar.jsx";
function ResultBox(props) {
  return (
    <>
      <div className="result-box">
        <h2>Kết quả kiểm tra:</h2>
        <p className="content">
          <strong className="title">File type: </strong>
          {props.result}
        </p>
      </div>
    </>
  );
}
export default ResultBox;
