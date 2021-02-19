import axios from 'axios';
import {
  USER_LOGIN_FAIL,
  USER_LOGIN_REQUEST,
  USER_LOGIN_SUCCESS,
  USER_LOGOUT,
  USER_REGISTER_REQUEST,
  USER_REGISTER_SUCCESS,
  USER_REGISTER_FAIL,
  USER_DETAILS_REQUEST,
  USER_DETAILS_SUCCESS,
  USER_DETAILS_FAIL,
  USER_UPDATE_PROFILE_REQUEST,
  USER_UPDATE_PROFILE_SUCCESS,
  USER_UPDATE_PROFILE_FAIL,
} from '../reducers/actionTypes';

export const login = (email, password) => async (dispatch) => {
  try {
    // dispatch the action first to reducers - this simply is going to be used for setting some state for a loading bar or spinner
    dispatch({
      type: USER_LOGIN_REQUEST,
    });
    const config = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const { data } = await axios.post(
      'http://127.0.0.1:5000/api/auth/login',
      { email, password }, // the data to send in the request
      config,
    );

    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data, // send this data as the payload for this action
    });
    // save the user information in local storage: contains the users id, name email, admin permission and token
    // we will want to load this initially (if it existed) into initial state in our store.js. See the code there
    localStorage.setItem('userInfo', JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_LOGIN_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const register = (name, email, password) => async (dispatch) => {
  try {
    // dispatch the action first to reducers - this simply is going to be used for setting some state for a loading bar or spinner
    dispatch({
      type: USER_REGISTER_REQUEST,
    });
    const config = {
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const { data } = await axios.post(
      'http://127.0.0.1:5000/api/auth/register',
      { name, email, password }, // the data to send in the request
      config,
    );

    dispatch({
      type: USER_REGISTER_SUCCESS,
      payload: data, // send this data as the payload for this action
    });

    // we want user automatically logged in with register so also dispatch that action and then set localstorage too
    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data,
    });
    // save the user information in local storage: contains the users id, name email, admin permission and token
    // we will want to load this initially (if it existed) into initial state in our store.js. See the code there
    localStorage.setItem('userInfo', JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_REGISTER_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

// get state allows us to get the state for the user info which contains the token when logged in!
export const getUserDetails = (id) => async (dispatch, getState) => {
  try {
    // dispatch the action first to reducers - this simply is going to be used for setting some state for a loading bar or spinner
    dispatch({
      type: USER_DETAILS_REQUEST,
    });

    // pull out the token from the state asscociated with this reducer (which is userLogin which then contains userInfo nested)
    const {
      userLogin: { userInfo },
    } = getState(); // get the current state in our redux store so we can pull out the usersIfnor which contains the ID needed to send the auth request to server to get private info

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    // Get the users info for the user signed in (id will be in state)
    const { data } = await axios.get(`/api/users/${id}`, config);

    dispatch({
      type: USER_DETAILS_SUCCESS,
      payload: data, // send this data as the payload for this action
    });
  } catch (error) {
    dispatch({
      type: USER_DETAILS_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const updateUserProfile = (user) => async (dispatch, getState) => {
  try {
    // dispatch the action first to reducers - this simply is going to be used for setting some state for a loading bar or spinner
    dispatch({
      type: USER_UPDATE_PROFILE_REQUEST,
    });

    // pull out the token from the state asscociated with this reducer (which is userLogin which then contains userInfo nested)
    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${userInfo.token}`,
      },
    };
    const { data } = await axios.put('/api/users/profile', user, config);

    dispatch({
      type: USER_UPDATE_PROFILE_SUCCESS,
      payload: data, // send this data as the payload for this action
    });

    // dispatch the login action to the store such that we can update the users name in the state after the other action above which updates it only for the state that its worrying about
    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data, // send this data as the payload for this action
    });

    // should update the users new name in local storage
    localStorage.setItem('userInfo', JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_UPDATE_PROFILE_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};

export const logout = () => (dispatch) => {
  localStorage.removeItem('userInfo'); // remove user info from the local storage
  dispatch({
    type: USER_LOGOUT,
  });
};
