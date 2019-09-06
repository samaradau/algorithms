
    let request = new XMLHttpRequest();
    
    request.open("GET", "http://dummy.restapiexample.com/api/v1/employees", true);

    request.onload = function() {
        let data = JSON.parse(this.response);
        let employeeConteiner = document.getElementById("employees");

        let viewEmployee = function(employee) {
            let rootNode = document.createElement("div");
            rootNode.className = "employee";
            rootNode.id = `employee_${employee.id}`;
            
            let viewEmployeeProperty = function(property) {
                let propertyNode = document.createElement("span");
                propertyNode.className = "employee__property";
                propertyNode.innerText = property;
                rootNode.appendChild(propertyNode);
            } 

            viewEmployeeProperty(employee.id);
            viewEmployeeProperty(employee.employee_name);
            viewEmployeeProperty(employee.employee_salary);
            viewEmployeeProperty(employee.employee_age);
            viewEmployeeProperty(employee.profile_image);

            employeeConteiner.appendChild(rootNode);
        } 

        data.forEach(employee => {
            viewEmployee(employee);
        });
    }
    
    request.send();
