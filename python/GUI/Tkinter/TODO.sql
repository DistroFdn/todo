USE master

CREATE DATABASE ToDo 

USE ToDo

IF  NOT EXISTS (SELECT * FROM sys.objects 
WHERE object_id = OBJECT_ID(N'[dbo].[Daily]') AND type in (N'U'))

BEGIN
CREATE TABLE [dbo].[Daily](
	id INT IDENTITY NOT NULL PRIMARY KEY,
	start_at DATETIME DEFAULT GETDATE() NOT NULL,
	end_at_date DATE DEFAULT GETDATE() NOT NULL,
	end_at_time TIME (0) NOT NULL,
	labels NVARCHAR(MAX) NOT NULL,
	descriptions NVARCHAR(MAX),
	) 

END

--DROP TABLE Daily

INSERT INTO Daily(end_at_time,labels,descriptions) 
VALUES('13:05',N'ریاضی ۲',N'خاک بر سر این استاد که انقدر تمرین میده')

SELECT * FROM Daily


