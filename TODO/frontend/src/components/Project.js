import React from "react";
import './bootstrap/css/bootstrap.min.css'

const ProjectItem = ({project}) => {
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
                {project.update_at}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
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
            </thead>
            <tbody>
            {projects.map((project) => <ProjectItem project={project} />)}
            </tbody>
        </table>
    )
} 

export default ProjectList;