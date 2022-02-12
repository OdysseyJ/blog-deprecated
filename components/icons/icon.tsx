import Image from 'next/image'

const imagePath = "/images/icons/"

type IconProps = {
    filename : string
    width: number
    height: number
}

const Icon : React.FC<IconProps> = ({filename, width, height})=>{
    return <Image
        src={imagePath+filename}
        alt="Photo"
        width={width}
        height={height}
        priority
        className="next-image"
    />

}


export default Icon