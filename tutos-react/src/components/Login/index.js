import React, { useState, Fragment } from 'react';
import { connect } from 'react-redux';
import Popup from 'reactjs-popup';
import * as selectors from '../../reducers';
import * as actions from '../../actions/auth';

import { SuccessBtn } from '../Buttons';

import './styles.css'; 


const Login = ({
    isLoading,
    error = null,
}) => {
    const [username, changeUsername] = useState('');
    const [password, changePassword] = useState('');
    return (
        <Popup trigger={<button className="popup">Login</button>} position="bottom center">
            <div className="popup-container">
                <p>
                    <input 
                        className="input-login"
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={e => changeUsername(e.target.value)}
                    />
                </p>
                <p>
                    <input 
                        className="input-login"
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={e => changePassword(e.target.value)}
                    />
                </p>
                <p>
                    {
                        isLoading ? (
                            <strong>{'Cargando...'}</strong>
                        ) : (
                            <SuccessBtn text={'Login'} action={actions.startLogin(username, password)} />
                        )
                    }
                </p>
                {
                    error && (
                    <p>
                        <strong className='error-text'>{ error }</strong>
                    </p>
                    )
                }
            </div>
        </Popup>
    );
};

export default connect(
    state => ({
        isLoading: selectors.getIsAuthenticating(state),
        error: selectors.getAuthenticatingError(state),
    }),
)(Login);