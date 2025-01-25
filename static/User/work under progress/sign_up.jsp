<%@page import="java.sql.*" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Set Username and Password</title>
    <style>
               body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        label {
            display: block;
            margin-top: 15px;
            font-weight: bold;
        }
        input, button {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
            <%
                try {
                    String userName = request.getParameter("username");
                    String password = request.getParameter("password");
                    String cpassword = request.getParameter("confirm-password");
                    String name = request.getParameter("name");
                    int age = Integer.parseInt(request.getParameter("age"));
                    String address = request.getParameter("address");
                    String gender = request.getParameter("gender");
                    String mobileNo = request.getParameter("mobile");
                    String emailId = request.getParameter("email");
                    String state = request.getParameter("state");
            
                     Connection con = null;
                    PreparedStatement signUpStmt = null;
                    PreparedStatement regDetailStmt = null;
                    try {
                        Class.forName("com.mysql.jdbc.Driver");
                        con=DriverManager.getConnection("jdbc:mysql://localhost:3306/srgc","root","sharmaji3.1415926");
                        //Statement statement=con.createStatement();
                        String signUpQuery = "INSERT INTO sign_up (user_name, password) VALUES (?, ?)";
                        signUpStmt = con.prepareStatement(signUpQuery);
                        signUpStmt.setString(1, userName);
                        signUpStmt.setString(2, password);
                        String regDetailQuery = "INSERT INTO registration_detail (user_name, name, address, age, gender, mobile_no, email_id, state) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
                        regDetailStmt = con.prepareStatement(regDetailQuery);
                        regDetailStmt.setString(1, userName);
                        regDetailStmt.setString(2, name);
                        regDetailStmt.setString(3, address);
                        regDetailStmt.setInt(4, age);
                        regDetailStmt.setString(5, gender);
                        regDetailStmt.setString(6, mobileNo);
                        regDetailStmt.setString(7, emailId);
                        regDetailStmt.setString(8, state);
                        if(password.equals(cpassword)) {
                            signUpStmt.executeUpdate();
                            regDetailStmt.executeUpdate();
                            out.println("<h3>Data inserted successfully!</h3>");
                            response.sendRedirect("/../applications/app5/Login/");
                        }
                        else {
                            out.println("password did not match with confirm password");
                        }
                    }
                    catch (SQLIntegrityConstraintViolationException e) {
                        out.println("<h3>Error: Duplicate user name or email ID. Please use unique values.</h3>");
                    }
                    finally {
                        if (regDetailStmt != null) regDetailStmt.close();
                        if (signUpStmt != null) signUpStmt.close();
                        if (con != null) con.close();
                    }
                }
                catch (Exception e) {
                    e.printStackTrace();
                    out.println("<h3>"+e.getMessage()+"</h3>");
                }
            %>
</body>
</html>
