import "./MetadataBox.css";

function InfoCard({ children }) {
  return (
    <section className="metadata">
      <dl className="info-card-header">
        <h1>Metadata information</h1>
        <div className="metadata-content">{children}</div>
      </dl>
    </section>
  );
}

export default InfoCard;
