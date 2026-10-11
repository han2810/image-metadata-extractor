import "./GoogleMap.css";

function GoogleMap({ latitude, longitude }) {
  const mapUrl = `https://www.google.com/maps?q=${latitude},${longitude}&z=16&output=embed`;

  return (
    <div className="google-map">
      <iframe
        src={mapUrl}
        width="100%"
        height="90%"
        allowFullScreen
        loading="lazy"
        title="Google Map"
      />
    </div>
  );
}

export default GoogleMap;
