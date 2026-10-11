import "./App.css";
import Home from "./pages/Home.jsx";
import ImageType from "./pages/Imagetype.jsx";
import ImageTypeResult from "./pages/ImageTypeResult.jsx";
import ImageDetail from "./pages/ImageDetail.jsx";
import ImageDetailResult from "./pages/ImageDetailResult.jsx";
import { Route, Routes } from "react-router-dom";
function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/checktype" element={<ImageType />} />
      <Route path="/checktype/result" element={<ImageTypeResult />} />
      <Route path="/checkdetail" element={<ImageDetail />} />
      <Route path="/checkdetail/result" element={<ImageDetailResult />} />
    </Routes>
  );
}
export default App;
