
import React, { Component } from 'react';

class Form extends React.Component {
	render() {
  	return (
    	<form>
        <input 
          type="text" 
          placeholder="Enter URL" 
          required
        />
        <button>Go!</button>
    	</form>
    );
  }
}

export default Form;