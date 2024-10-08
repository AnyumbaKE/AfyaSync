import React, { useRef, useState } from "react";
import { useLoginMutation } from "./authApiSlice";
import * as Yup from "yup";
import { Form, Formik, useField } from "formik";
import LoadingScreen from '../../components/LoadingScreen';
import Slider from './Slider';
import Footer from './Footer';

const label_style = "pl-2 text-lg font-normal";
const input_style = "block rounded-xl h-7 w-60 mb-1 bg-gray focus:outline-none focus:ring-2 focus:ring-lightBlue";
const button_style = "h-10 w-[100%] px-4 py-2 text-lg rounded-md shadow-md focus:outline-none focus:ring focus:ring-gray-400";

const MyTextInput = ({ label, ...props }) => {
  const [field, meta] = useField(props);
  return (
    <div className="">
      <label className={`${label_style}`} htmlFor={props.id || props.name}>
        {label}
      </label>
      <input
        autoComplete="off"
        className={`input p-5 ${input_style} ${meta.touched && meta.error ? "border border-red animate-shake" : ""}`}
        {...field}
        {...props}
      />
      {meta.touched && meta.error ? (
        <div className="error pl-5 text-red">{meta.error}</div>
      ) : null}
    </div>
  );
};

const Login = () => {
  const errRef = useRef();
  const [errMsg, setErrMsg] = useState("");
  const [errCode, setErrCode] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const [login] = useLoginMutation();

  const authLink = process.env.REACT_APP_AUTH_URL;
  const docLink = process.env.REACT_APP_DOC_URL;
  const nurseLink = process.env.REACT_APP_NUR_URL;
  const patientLink = process.env.REACT_APP_PAT_URL;
  const pharmacyLink = process.env.REACT_APP_PHA_URL;

  const handleRedirect = (userId, role, token, username) => {
    const params = `token=${token}&role=${role}&id=${userId}&username=${username}`;
    setIsLoading(false);
    if (role === "doctor" || role === "admin")
      window.location.href = `${docLink}/dashboard?${params}`;
    else if (role === "nurse")
      window.location.href = `${nurseLink}/dashboard?${params}`;
    else if (role === "patient")
      window.location.href = `${patientLink}/dashboard?${params}`;
    else if (role === "pharmacist")
      window.location.href = `${pharmacyLink}/dashboard?${params}`;
    else window.location.href = `${authLink}/dashboard?${params}`;
    return null;
  };

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <div className="flex h-screen">
      <div className="w-1/2 h-full">
        <Slider /> {/* Display the slider on the left side */}
      </div>
      <div className="w-1/2 h-full flex items-center justify-center bg-white">
        <div className="w-full max-w-md p-8">
          <Formik
            initialValues={{
              username: "",
              password: "",
            }}
            validationSchema={Yup.object({
              username: Yup.string().required("Field Required"),
              password: Yup.string().required("Field Required"),
            })}
            onSubmit={async (values, { setSubmitting, resetForm }) => {
              setIsLoading(true);
              try {
                const userData = await login(values).unwrap();
                handleRedirect(userData.id, userData.role, userData.token, userData.username);
                resetForm();
              } catch (err) {
                setIsLoading(false);
                if (err?.originalStatus) {
                  setErrCode(err?.status);
                  setErrMsg("No Server Response");
                } else {
                  setErrCode(err?.status);
                  setErrMsg(err.data.error);
                }
                if (errMsg && errRef.current) {
                  errRef.current.focus();
                }
              }
            }}
          >
            <div className="flex flex-col justify-center items-center">
              <h1 className="text-xl font-semibold mb-5">Login</h1>
              <Form>
                <div className="mb-5">
                  <MyTextInput label={"Username"} name="username" type="text" />
                  {errMsg && (
                    <span
                      ref={errRef}
                      className={`${errMsg ? "errmsg" : "hidden"} text-red error pl-5`}
                      aria-label=""
                    >
                      {errMsg}
                    </span>
                  )}
                </div>
                <div className="mb-5">
                  <MyTextInput
                    label={"Password"}
                    name="password"
                    type="password"
                  />
                </div>
                <button
                  className={`bg-lightBlue text-white ${button_style}`}
                  type="submit"
                >
                  Login
                </button>
              </Form>
            </div>
          </Formik>
        </div>
      </div>
      <Footer /> {/* Add the footer component */}
    </div>
  );
};

export default Login;
