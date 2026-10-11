import "./UploadBox.css";
import { useState } from "react";
import { useNavigate } from "react-router";
function ImageType(props) {
  const [file, setFile] = useState(null);
  const [fileSize, setFileSize] = useState(null);
  let navigate = useNavigate();
  function handleFileChange(event) {
    const selectedFile = event.target.files[0];
    const imagePreviewURL = URL.createObjectURL(selectedFile);
    const imagePreview = document.getElementById("imagePreview");
    const imageBox = document.getElementById("image-box");
    const uploadPage = document.getElementById("upload-page");
    const lableForInput = document.getElementById("label-for-input");
    uploadPage.style.display = "grid";
    uploadPage.style.gridTemplateColumns = "1fr 1fr";
    imageBox.style.display = "flex";
    imagePreview.src = imagePreviewURL;
    lableForInput.textContent = "📁 Chọn file khác";
    setFileSize((selectedFile.size / (1024 * 1024)).toFixed(2));
    setFile(selectedFile);
  }
  async function handleSubmit(event) {
    event.preventDefault();
    if (!file) {
      alert("Vui lòng chọn file!");
      return;
    }
    const formData = new FormData();
    formData.append("file", file);
    const response = await fetch(props.url, {
      method: "POST",
      body: formData,
    });
    const data = await response.json();
    navigate("result", { state: data });
  }
  return (
    <>
      <h1 className="home-h1">Image investigator</h1>
      <div id="upload-page">
        <div className="upload-box">
          <h2 className="function-name">{props.function}</h2>
          <form onSubmit={handleSubmit}>
            <div className="file-upload-wrapper">
              <input
                type="file"
                id="custom-file-input"
                className="hidden-file-input"
                onChange={handleFileChange}
              />
              <label
                id="label-for-input"
                htmlFor="custom-file-input"
                className="btn-choose-file"
              >
                📁 Chọn tệp tải lên
              </label>
            </div>
            <button type="submit" className="btn-submit">
              Kiểm tra
            </button>
          </form>
        </div>
        <div id="image-box">
          <img id="imagePreview" src="a" alt="Preview image" />
          {file && (
            <div className="file-name">
              <b>Sẵn sàng tải lên </b>
              <span>Kích thước: {fileSize} MB</span>
            </div>
          )}
        </div>
      </div>
    </>
  );
}

export default ImageType;
