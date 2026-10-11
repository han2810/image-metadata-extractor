import Navbar from "../components/Navbar.jsx";
import UploadBox from "../components/UploadBox.jsx";
function ImageLocation() {
  return (
    <>
      <Navbar />
      <UploadBox
        url="http://127.0.0.1:5000/checkdetail"
        function="Image metadata reader"
      />
    </>
  );
}
export default ImageLocation;
