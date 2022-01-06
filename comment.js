import {useRouter} from "next/router";
import {useEffect} from "react";


const Comment = () => {
    const router = useRouter()

    console.log(router.pathname)
    console.log(router.asPath)
    useEffect(()=>{
        const is_commentable = router.pathname.split("/").length >= 3;
        if(is_commentable){
            (function() { // DON'T EDIT BELOW THIS LINE
                var d = document, s = d.createElement('script');
                s.src = 'https://aaronjeong.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
                })();
        }
    },[])

    return (<div id="disqus_thread"></div>)
}

export default Comment 
