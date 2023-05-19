import frame from '../assets/frames/main_frame.png';

const Home = () => {
    return (
        <div id="home-frame">
            <div id="home-contents" className="" style={{zIndex: 4}}>
                <h1>gallerify</h1>
                <p>what does your music library gallery look like?</p>
                <button>test button</button>  
            </div>
            {/* <img src={frame}/> */}
        </div>
    );
};

export default Home;