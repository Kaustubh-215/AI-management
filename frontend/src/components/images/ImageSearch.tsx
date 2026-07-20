interface ImageSearchProps {
  value: string;
  onChange: (value: string) => void;
}

export default function ImageSearch({
  value,
  onChange,
}: ImageSearchProps) {
  return (
    <input
      type="text"
      placeholder="Search images..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="w-full border rounded-lg p-3"
    />
  );
}
