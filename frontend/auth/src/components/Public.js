import { Link } from "react-router-dom";

const Public = () => {
    const dummy = (
        <section className="m-0 p-0 relative bg-gray">
            <header className="fixed top-0 left-0 h-20 w-full items-center flex bg-lightBlue text-white">
                <span className="ml-auto pr-10 text-lg">
                    <Link to="/login">Login</Link>
                </span>
            </header>
            <main className="pt-20">
                <section className="h-[80vh] bg-white"></section>
            </main>
            <footer className="absolute h-20 bottom-0 left-0 text-white w-full bg-lightBlue">
                <span>Footer</span>
            </footer>
        </section>
    );
    return dummy;
};
export default Public;