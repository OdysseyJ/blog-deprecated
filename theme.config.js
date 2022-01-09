import Comment from './comment'

const YEAR = new Date().getFullYear()

export default {
  readMore: '자세히 보기',
  footer: (
    <>
        <small style={{ display: 'block', marginTop: '8rem' }}>
          <time>{YEAR}</time>
          <a href="/feed.xml">RSS</a>
          <style jsx>{`
            a {
              float: right;
            }
            @media screen and (max-width: 480px) {
              article {
                padding-top: 2rem;
                padding-bottom: 4rem;
              }
            }
          `}</style>
        </small>
    </>
  ),
  postFooter: (
    <>
      <Comment/>
    </>
  ),
}
