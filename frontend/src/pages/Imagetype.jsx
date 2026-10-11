import "./Home.css";
import Navbar from "../components/Navbar";
import UploadBox from "../components/UploadBox";
function ImageType() {
  return (
    <>
      <Navbar />
      <UploadBox
        url="http://127.0.0.1:5000/checktype"
        function="Check image type"
      />
    </>
  );
}

export default ImageType;
