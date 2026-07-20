interface ImageSortProps {
  value: string;
  onChange: (value: string) => void;
}

export default function ImageSort({
  value,
  onChange,
}: ImageSortProps) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="border rounded-lg p-3"
    >
      <option value="newest">Newest</option>
      <option value="oldest">Oldest</option>
      <option value="az">A-Z</option>
      <option value="za">Z-A</option>
    </select>
  );
}
