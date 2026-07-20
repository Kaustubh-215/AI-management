interface FilterOption {
  name: string;
  count: number;
}

interface ImageFilterProps {
  value: string;
  onChange: (value: string) => void;
  filters: FilterOption[];
}

export default function ImageFilter({
  value,
  onChange,
  filters,
}: ImageFilterProps) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className="border rounded-lg p-3 w-full"
    >
      <option value="">
        All Files
      </option>

      {filters.map((filter) => (
        <option
          key={filter.name}
          value={filter.name}
        >
          {filter.name.toUpperCase()} ({filter.count})
        </option>
      ))}
    </select>
  );
}
