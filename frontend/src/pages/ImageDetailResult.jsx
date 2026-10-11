import "./ImageDetailResult.css";
import { useLocation } from "react-router-dom";
import GoogleMap from "../components/GoogleMap.jsx";
import MetadataBox from "../components/MetadataBox.jsx";
import Navbar from "../components/Navbar";
function Result() {
  let latitude = "30";
  let longitude = "45";
  let GPSLatitudeRef = "N";
  let GPSLongitudeRef = "E";
  const location = useLocation();
  const dataList = location.state;
  const metadataList = dataList.map((object) => {
    let displayValue = object.value;
    if (object.name == "GPSLatitude") {
      latitude = `${object.value[0]}°${object.value[1]}'${object.value[2]}"`;
      displayValue = latitude;
    } else if (object.name == "GPSLongitude") {
      longitude = `${object.value[0]}°${object.value[1]}'${object.value[2]}"`;
      displayValue = longitude;
    } else if (object.name == "GPSLongitudeRef") {
      GPSLongitudeRef = object.value;
    } else if (object.name == "GPSLatitudeRef") {
      GPSLatitudeRef = object.value;
    }
    return (
      <div className="metadata-line" key={object.name}>
        <dt className="property-name">{object.name}</dt>
        <dd className="property-value">{displayValue}</dd>
      </div>
    );
  });
  latitude = latitude + GPSLatitudeRef;
  longitude = longitude + GPSLongitudeRef;
  return (
    <>
      <Navbar />
      <div className="detail-result-page">
        <div className="result-map">
          {latitude && longitude && (
            <GoogleMap latitude={latitude} longitude={longitude} />
          )}
        </div>
        <MetadataBox>{metadataList}</MetadataBox>
      </div>
    </>
  );
}

export default Result;
