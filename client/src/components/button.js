import React from "react";

// https://devcamp.com/trails/comprehensive-react-development-tutorial/campsites/react-project-two-build-birthday-countdown-application/guides/how-to-create-functional-button-component-react

const Button = ({ children, buttonType }) => {
    var buttonStyle;
    switch (buttonType) {
        case 'primary':
            buttonStyle = {
                backgroundColor: '#3B7F98',
            }
            break;
        case 'time':
            buttonStyle = {
                backgroundColor: 'black'
            }
    }
    return (
        <>
            <button className="button" style={buttonStyle}>
                {children}
            </button>
        </>
    )
}

{/* <div>
{isLoggedIn ? (
  <h1>Welcome back!</h1>
) : (
  <h1>Please sign up.</h1>
)}
</div> */}

// https://blog.bitsrc.io/5-ways-to-style-react-components-in-2019-30f1ccc2b5b
const primaryStyle = {
    backgroundColor: '#3B7F98',
}

const timeStyle = {
    borderWidth: 'thick',
    borderColor: '#FFFAE8',
    backgroundColor: '#472C1B'
}

export default Button;