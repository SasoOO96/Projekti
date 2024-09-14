#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <sha.h>
#include<QDebug>
#include <QVariant>
#include <QSqlQuery>
#include <QSqlError>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connectToDatabase();
}

MainWindow::~MainWindow()
{
    db.close();
    delete ui;
}


void MainWindow::connectToDatabase()
{
   QString serverName = "localhost";
   QString databaseName = "FileHasherDB";

   QString connectionString = QString("DRIVER={SQL Server};SERVER=%1;DATABASE=%2;Trusted_Connection=yes;")
       .arg(serverName)
       .arg(databaseName);

   QSqlDatabase db = QSqlDatabase::addDatabase("QODBC");
   db.setDatabaseName(connectionString);



   if (!db.open()) {
       // QMessageBox::critical(this, "Database Error", db.lastError().text());
        return;
    }

    QSqlQuery query;
    query.exec("CREATE TABLE IF NOT EXISTS FileHashes ("
               "Id INT PRIMARY KEY IDENTITY(1,1), "
               "Filename NVARCHAR(255) NOT NULL, "
               "Hash NVARCHAR(64) NOT NULL)");

    if (query.lastError().isValid()) {
       // QMessageBox::critical(this, "Database Error", query.lastError().text());
    }
}
void MainWindow::on_pushButton_clicked()
{
   QString filePath = QFileDialog::getOpenFileName(this, "Open File", "", "All Files (*.*)");

   QFileInfo fileInfo(filePath);
   QString fileName = fileInfo.fileName();

    if (!fileName.isEmpty()) {
        ui->label_2->setText(fileName);
    }

}

bool MainWindow::checkAndInsertUser(const QString &filename, const QString &hash) {
    if (checkUserExists(filename,hash)) {
      //  qDebug() << "User already exists!";
        QMessageBox::about(this, "Information", "Datoteka vec postoji u bazi podataka!");
        return false;
    } else {
        return insertUser(filename, hash);
    }
}
bool MainWindow::insertUser(const QString &filename, const QString &hash) {
    QSqlQuery query;
    query.prepare("INSERT INTO FileHashes (Filename, Hash) VALUES (:filename, :hash)");
    query.bindValue(":filename", filename);
    query.bindValue(":hash", hash);

    if (!query.exec()) {
       // qDebug() << "Insert error: " << query.lastError();
         QMessageBox::critical(this, "Database Error", query.lastError().text());
        return false;
    } else {
        QMessageBox::information(this, "Success", "File hashed and stored successfully");
    }
    return true;
}
bool MainWindow::checkUserExists(const QString &filename, const QString &hash)
{
    QSqlQuery query;
    query.prepare("SELECT COUNT(*) FROM FileHashes WHERE Filename = :filename AND Hash = :hash");
    query.bindValue(":filename", filename);
    query.bindValue(":hash",hash);

    if(!query.exec())
    {
        qDebug()<<"Query execution error: "<< query.lastError();
        return false;
    }
    if(query.next()){
        int count = query.value(0).toInt();
        return count > 0;
    }
    return false;
}

void MainWindow::on_pushButton_2_clicked()
{
    string message = ui->label_2->text().toStdString();
    string hash = SHA::get_hash(message);
    ui->label_4->setText(QString::fromStdString(hash));

}

void MainWindow::on_pushButton_3_clicked()
{
    // hashAndStoreFile(ui->label_2->text());
    checkAndInsertUser(ui->label_2->text(),ui->label_4->text());
}


void MainWindow::on_pushButton_4_clicked()
{
    QString fileName = ui->label_2->text();//.toStdString()
    QString hash = ui->label_4->text();
    if(checkUserExists(fileName,hash)){
        ui->label_5->setText("Datoteka POSTOJI u bazi podataka.");
    } else {
          ui->label_5->setText("Datoteka NE POSTOJI u bazi podataka.");
    }
}
/*void MainWindow::hashAndStoreFile(const QString &filename)
{
    QFile file(filename);
    if (!file.open(QIODevice::ReadOnly)) {
        QMessageBox::critical(this, "File Error", "Cannot open file for reading");
        return;
    }

    QString hash = ui->label_4->text();
   if(!checkUserExists(filename,hash)){
        QSqlQuery query;
        query.prepare("INSERT INTO FileHashes (Filename, Hash) VALUES (:filename, :hash)");
        query.bindValue(":filename", filename);
        query.bindValue(":hash", hash);
        if (!query.exec()) {
            QMessageBox::critical(this, "Database Error", query.lastError().text());
        } else {
            QMessageBox::information(this, "Success", "File hashed and stored successfully");
        }
    } else {
        ui->label_5->setText("Ne mozete je dodati jer vec postoji u bazi podataka!");
    }
}*/
