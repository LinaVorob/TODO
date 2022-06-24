import React from "react";
import './bootstrap/css/bootstrap.min.css'

class ProjectForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {name: '', repohref: '', user: props.users[0]?.uuid}
    }
  
    handleChange(event) 
    {    
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );  
    }

    handleSubmit(event) {
      this.props.createProject(this.state.name, this.state.repohref, this.state.user)
      event.preventDefault()
    }
  
    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <div className="form-group">
            <label for="name">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name} onChange={(event)=>this.handleChange(event)} />      
                <br></br>  
            </div>

            <div className="form-group">
            <label for="repohref">repository</label>
                <input type="text" className="form-control" name="repohref" value={this.state.repohref} onChange={(event)=>this.handleChange(event)} />      
                <br></br>  
            </div>
          
        <div className="form-group">
            <label for="user">author</label>
    
            <select name="user" className='form-control' onChange={(event)=>this.handleChange(event)}>
                {this.props.users.map((item)=><option value={item.uuid}>{item.username}</option>)}
            </select>       

          </div>
          <input type="submit" className="btn btn-primary" value="Save" />
        </form>
      );
    }
  }

export default ProjectForm;