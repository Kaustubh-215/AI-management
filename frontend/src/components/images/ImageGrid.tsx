import ImageCard from "./ImageCard";

interface Props {

  images: any[];

  onDelete: () => void;

  selectedImages: number[];

  setSelectedImages: React.Dispatch<
    React.SetStateAction<number[]>
  >;

  view: "grid" | "list";
}

export default function ImageGrid({

  images,

  onDelete,

  selectedImages,

  setSelectedImages,

  view,

}: Props) {

  return (

    <div

      className={

        view === "grid"

          ? "grid md:grid-cols-2 lg:grid-cols-3 gap-6"

          : "space-y-4"

      }

    >

      {images.map((image) => (

        <ImageCard

          key={image.id}

          image={image}

          onDelete={onDelete}

          showCheckbox

          checked={selectedImages.includes(image.id)}

          onSelect={(checked) => {

            if (checked) {

              setSelectedImages(

                [...selectedImages, image.id]

              );

            } else {

              setSelectedImages(

                selectedImages.filter(

                  (id) => id !== image.id

                )

              );
            }
          }}

        />

      ))}

    </div>
  );
}
