import mysql.connector
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

def create_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Suhaib@12345",
            database="employee_info",
            auth_plugin="mysql_native_password"
        )
        return connection
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

@app.get("/connect")
def check_connection():
    """Check if database connection can be established"""
    try:
        connection = create_connection()
        if connection.is_connected():
            connection.close()
            return {"status": "Connection successful"}
        return JSONResponse(content={"status": "Connection failed"}, status_code=500)
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")

@app.get("/team-members/")
def read_team_members():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        
        try:
            cursor.execute("SELECT * FROM team_members")
            result = cursor.fetchall()
            
            team_members = [
                {"Name": row[0], "Role": row[1], "Email": row[2], "Age": row[3]} 
                for row in result
            ]
            
            return JSONResponse(content={"team_members": team_members})
            
        except mysql.connector.Error as e:
            raise HTTPException(status_code=500, detail=f"Query execution failed: {e}")
            
        finally:
            cursor.close()
            connection.close()
            
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# mycursor=mydb.cursor()

# sql="SELECT * FROM team_members"
# mycursor.execute(sql)

# result = mycursor.fetchall()
# for row in result:
#     print(row)