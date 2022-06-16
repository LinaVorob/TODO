import React from "react";
import './bootstrap/css/bootstrap.min.css';
import {Link} from 'react-router-dom';

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.repohref}
            </td>
            <td>
                {project.user.username}
            </td>
            <td>
                {project.updated_at}
            </td>
            <td>
                <button onClick={() => deleteProject(project.uuid)} type='button'>X</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
        <table class="table .table-bordered">
            <thead class="table-light">
                <th>
                    Name
                </th>
                <th>
                    Repository
                </th>
                <th>
                    Author
                </th>
                <th>
                    Updated
                </th>
                <th>
                </th>
            </thead>
            <tbody>
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
            </tbody>
        </table>
        <Link to='/projects/create/'>Create new project</Link>
        </div>
    )
} 

export default ProjectList;