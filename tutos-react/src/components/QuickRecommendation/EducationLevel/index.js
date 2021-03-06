import React, {Fragment} from 'react';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import './styles.css'; 
import '../../../index.css';
// import '../../../normalize.css';

import Navbar from '../../Navbar';


const QuickRecommendationEducationLevel = ({state}) => {
    return (
        <div className="page">
        <Navbar/>
            <div className="educationLevel_form">
                <h2>¿Para qué nivel educativo buscas la tutoría?</h2>
                <div className="schoolOption">
                    <input type="radio" className="radioButton" value="school"/>
                    <label for="school" className="labelj">Colegio</label>
                </div>
                <div className="collegeOption"> 
                    <input type="radio" className="radioButton" value="college"/>
                    <label for="college">Universidad</label>
                </div>
                <div className="noSpecificationOption">
                    <input type="radio" className="radioButton" value="noSpecification"/>
                    <label for="noSpecification">Sin especificar</label>
                </div>

                <div>
                <Link to='/quick-recommendation/location'>
                    <a className="back">Atrás</a>
                </Link>
                <Link to='/quick-recommendation/schedule'>
                    <button type="button" className="next">Siguiente</button>
                </Link>
                </div>
            </div>
        </div>
    );
};

export default connect(
    (state) => ({
        state: state,
    })
)(QuickRecommendationEducationLevel);
