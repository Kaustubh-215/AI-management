import { useEffect, useMemo, useState } from "react";

import DashboardLayout from "@/components/layout/DashboardLayout";

import ImageGrid from "@/components/images/ImageGrid";
import ImageSearch from "@/components/images/ImageSearch";
import ImageFilter from "@/components/images/ImageFilter";
import ImageSort from "@/components/images/ImageSort";
import LoadingGrid from "@/components/images/LoadingGrid";
import EmptyState from "@/components/images/EmptyState";

import {
  getImages,
  bulkDeleteImages,
} from "@/services/image.service";

import { getFilters } from "@/services/filterService";

import {
  Trash2,
  LayoutGrid,
  List,
} from "lucide-react";

export default function Images() {

  const [images, setImages] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("");
  const [sort, setSort] = useState("newest");

  const [filters, setFilters] = useState<any[]>([]);

  const [selectedImages, setSelectedImages] =
    useState<number[]>([]);

  const [view, setView] =
    useState<"grid" | "list">("grid");

  const loadImages = async () => {

    try {

      setLoading(true);

      const data = await getImages();

      setImages(data);

    } catch (err) {

      console.error(err);

    } finally {

      setLoading(false);

    }
  };

  const loadFilters = async () => {

    try {

      const data = await getFilters();

      setFilters(data.filters);

    } catch (err) {

      console.error(err);

    }
  };

  useEffect(() => {

    loadImages();

    loadFilters();

  }, []);

  const handleBulkDelete = async () => {

    if (selectedImages.length === 0) {

      alert("Select files first");

      return;
    }

    const ok = window.confirm(

      `Delete ${selectedImages.length} files?`

    );

    if (!ok) {

      return;
    }

    try {

      await bulkDeleteImages(selectedImages);

      setSelectedImages([]);

      await loadImages();

      await loadFilters();

    } catch (e) {

      console.error(e);

      alert("Bulk delete failed");
    }
  };

  const filteredImages = useMemo(() => {

    let data = [...images];

    if (search) {

      data = data.filter((img) =>
        img.original_filename
          .toLowerCase()
          .includes(search.toLowerCase())
      );
    }

    if (filter) {

      data = data.filter(

        (img) =>

          img.file_category?.toLowerCase() ===

          filter.toLowerCase()
      );
    }

    switch (sort) {

      case "az":

        data.sort((a, b) =>

          a.original_filename.localeCompare(

            b.original_filename
          )
        );

        break;

      case "za":

        data.sort((a, b) =>

          b.original_filename.localeCompare(

            a.original_filename
          )
        );

        break;

      case "oldest":

        data.reverse();

        break;
    }

    return data;

  }, [images, search, filter, sort]);

  return (

    <DashboardLayout>

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-3xl font-bold">

          My Files

        </h1>

        <div className="flex gap-3">

          <button

            onClick={() => setView("grid")}

            className={`p-3 rounded-xl ${
              view === "grid"
                ? "bg-blue-600 text-white"
                : "bg-gray-200"
            }`}

          >

            <LayoutGrid size={18} />

          </button>

          <button

            onClick={() => setView("list")}

            className={`p-3 rounded-xl ${
              view === "list"
                ? "bg-blue-600 text-white"
                : "bg-gray-200"
            }`}

          >

            <List size={18} />

          </button>

          {selectedImages.length > 0 && (

            <button

              onClick={handleBulkDelete}

              className="bg-red-600 text-white px-5 py-3 rounded-xl flex gap-2"

            >

              <Trash2 size={18} />

              Delete ({selectedImages.length})

            </button>

          )}

        </div>

      </div>

      <div className="grid md:grid-cols-3 gap-4 mb-8">

        <ImageSearch
          value={search}
          onChange={setSearch}
        />

        <ImageFilter
          value={filter}
          onChange={setFilter}
          filters={filters}
        />

        <ImageSort
          value={sort}
          onChange={setSort}
        />

      </div>

      {loading ? (

        <LoadingGrid />

      ) : filteredImages.length === 0 ? (

        <EmptyState />

      ) : (

        <ImageGrid

          images={filteredImages}

          view={view}

          selectedImages={selectedImages}

          setSelectedImages={setSelectedImages}

          onDelete={async () => {

            await loadImages();

            await loadFilters();
          }}

        />

      )}

    </DashboardLayout>
  );
}
