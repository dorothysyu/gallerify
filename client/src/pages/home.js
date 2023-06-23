import frame from '../assets/frames/main_frame.png';
import Button from '../components/button';
const Home = () => {
    return (
        <div id="home-frame">
            <div id="home-contents" className="" style={{ zIndex: 4 }}>
                <h1>gallerify</h1>
                <p>what does your music library gallery look like?</p>
                <Button
                    buttonType={'primary'}
                    >
                    gallerify me!
                </Button>
            </div>
        </div>
    );
};

export default Home;