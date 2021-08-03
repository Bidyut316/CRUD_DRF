# CRUD_DRF
CRUD Using Django Rest Framework

  <h1 align="center">Django Rest Framework | CRUD</h1>
  <h3>The main entity is: </h3>
  <table>
    <tr>
      <td>
        <li>Student</li>
      </td>
    </tr>
  </table>
  <h3>Main tools and modules: </h3>
  <ul>
    <li>Django</li>
    <li>djangorestframework</li>
    <li>PostgreSQL</li>
  </ul>


  <h3>The API(s) are:</h3>
  <table style="width:100%">
    <tr>
      <th>Method</th>
      <th>Url</th>
      <th>Data</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>Get</td>
      <td>apis/</td>
      <td>-</td>
      <td>Return all api Urls</td>
    </tr>
    <tr>
      <td>Get</td>
      <td>students/</td>
      <td>-</td>
      <td>Get all student details</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>add-student/id/</td>
      <td>
        {<br>
        "name": String,<br>
        "email": email,<br>
        "sex": String,<br>
        "age": Positive Integer,<br>
        "mobile": String,<br>
        "city": String<br>
        }
      </td>
      <td>Add student Details</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>update-student/id/</td>
      <td>
        {<br>
        "name": String,<br>
        "email": email,<br>
        "sex": String,<br>
        "age": Positive Integer,<br>
        "mobile": String,<br>
        "city": String<br>
        }
      </td>
      <td>Update student data</td>
    </tr>
    <tr>
      <td>Delete</td>
      <td>delete-student/id/</td>
      <td>-</td>
      <td>Delete student record by id</td>
    </tr>

  </table>


